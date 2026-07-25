Option Explicit

Dim fso: Set fso = CreateObject("Scripting.FileSystemObject")
Dim shell: Set shell = CreateObject("WScript.Shell")

If WScript.Arguments.Count < 2 Then
    WScript.Echo "Usage: cscript //nologo Export-TurboCADStep.vbs <input.tcw> <output-dir> [visible]"
    WScript.Quit 1
End If

Dim inputFile: inputFile = WScript.Arguments(0)
Dim outputDir: outputDir = WScript.Arguments(1)
Dim visible: visible = True
If WScript.Arguments.Count >= 3 Then visible = CBool(WScript.Arguments(2))

If IsProcessRunning("tcw27.exe") Then
    WScript.Echo "TurboCAD is already running. Please close all TurboCAD applications before starting this script."
    WScript.Quit 1
End If

Dim projectBaseName: projectBaseName = BaseName(inputFile)
Dim blocksDir: blocksDir = BuildPath(outputDir, projectBaseName & "-blocks")
Dim tempDir: tempDir = BuildPath(outputDir, "_tcw-temp")
EnsureFolder outputDir
EnsureFolder blocksDir
EnsureFolder tempDir

Dim runId: runId = TimeStampId()
Dim workFile: workFile = BuildPath(tempDir, BaseName(inputFile) & "-working-" & runId & ".tcw")

If fso.FileExists(workFile) Then fso.DeleteFile workFile, True
fso.CopyFile inputFile, workFile, True

Dim app: Set app = CreateObject("TurboCAD.Application")
app.Visible = visible
Dim tcProcessId: tcProcessId = app.GetProcessId()

Dim workDoc: Set workDoc = app.Drawings.Open(workFile)

SaveStep workDoc, BuildPath(outputDir, projectBaseName & ".stp")

Dim i, blockObj, blockName, blockPath
For i = 0 To workDoc.Blocks.Count - 1
    Set blockObj = workDoc.Blocks.Item(i)
    blockName = SafeName(GetBlockName(blockObj, i + 1))
    blockPath = BuildPath(blocksDir, blockName & ".stp")

    ClearGraphics workDoc
    InsertBlock workDoc, blockObj, blockName, i
    SaveStep workDoc, blockPath
Next

CloseAllDrawings app
SafeQuitInstance app, tcProcessId
Set app = Nothing

fso.DeleteFile workFile, True

WScript.Echo "Finished."

' =====================================================================
' Methode zum sicheren Beenden einer spezifischen TurboCAD-Instanz
' =====================================================================
Sub SafeQuitInstance(ByRef tcApp, ByVal tcProcessId)
    If IsObject(tcApp) Then
        If Not tcApp Is Nothing Then
            Set tcApp = Nothing
        End If
    End If

    If CLng(tcProcessId) > 0 Then
        shell.Run "cmd /c taskkill /F /PID " & CStr(tcProcessId) & " >nul 2>&1", 0, True
    End If
End Sub

Sub CloseAllDrawings(app)
    Dim docIndex, openDoc
    For docIndex = app.Drawings.Count - 1 To 0 Step -1
        Set openDoc = app.Drawings.Item(docIndex)
        openDoc.Saved = True
        openDoc.Close False
    Next
End Sub

Sub ClearGraphics(doc)
    doc.Graphics.Clear
    doc.Views.Refresh
End Sub

Sub InsertBlock(doc, blockObj, blockName, blockIndex)
    Dim insertedGraphic
    Set insertedGraphic = doc.Graphics.AddBlockInsertion(blockName, 0, 0, 0, 1, 1, 1, 0)

    insertedGraphic.Explode
    doc.Views.Refresh
End Sub

Sub SaveStep(entity, outPath)
    If fso.FileExists(outPath) Then
        fso.DeleteFile outPath, True
    End If

    WScript.Echo "Writing: " & outPath
    entity.SaveCopyAs outPath, "IMSIGX.STP.10"

    If Not fso.FileExists(outPath) Then
        WScript.Echo "SaveStep(" & outPath & "): file was not written."
        WScript.Quit 1
    End If
End Sub

Sub EnsureFolder(path)
    If Not fso.FolderExists(path) Then fso.CreateFolder path
End Sub

Function BuildPath(parent, child)
    BuildPath = fso.BuildPath(parent, child)
End Function

Function BaseName(path)
    BaseName = fso.GetBaseName(path)
End Function

Function SafeName(value)
    Dim name: name = value
    name = Replace(name, "\", "_")
    name = Replace(name, "/", "_")
    name = Replace(name, ":", "_")
    name = Replace(name, "*", "_")
    name = Replace(name, "?", "_")
    name = Replace(name, Chr(34), "_")
    name = Replace(name, "<", "_")
    name = Replace(name, ">", "_")
    name = Replace(name, "|", "_")
    If Trim(name) = "" Then name = "unnamed-block"
    SafeName = name
End Function

Function GetBlockName(blockObj, index)
    GetBlockName = blockObj.Name
End Function

Function IsProcessRunning(processName)
    Dim wmi: Set wmi = GetObject("winmgmts:\\.\root\cimv2")
    Dim processList: Set processList = wmi.ExecQuery("Select ProcessId from Win32_Process Where Name='" & processName & "'")
    IsProcessRunning = (processList.Count > 0)
End Function

Function TimeStampId()
    Dim d: d = Now
    TimeStampId = Year(d) & Right("0" & Month(d), 2) & Right("0" & Day(d), 2) & "-" & _
        Right("0" & Hour(d), 2) & Right("0" & Minute(d), 2) & Right("0" & Second(d), 2)
End Function