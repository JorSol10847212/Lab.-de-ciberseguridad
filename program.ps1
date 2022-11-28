$tarea = New-ScheduledTaskAction -Execute 'send_sysinfo.ps1'
$trigger = New-ScheduledTasktrigger -Once -At 05:35pm



register-ScheduledTask -Action $tarea -Trigger $trigger -TaskPath "MisTareas" -TaskName "Enviar sysinfo" -Description "Envio de información del sistema"