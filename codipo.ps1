## Jorge Andrés
## 01/10/2022
Clear-Host
Write-Host "Bienvenido a un ejemplo de codificación / decodificación base64 usando powershell" -ForegrounColor Green
Write-Host "Codificando un archivo de texto"
#
# Se va a leer el contenido del archivo de texto
#
$inputfile = "C:\Users\jorge\Desktop\Scripts07_1850014\secret.txt"
$fc = Get-Content $inputfile
$GB = [System.Text.Encoding]::UTF8.Getbytes($fc)
$etext = [System.Convert]::ToBase64String($GB)
Write-Host "El contenido del archivo CODIFICADO es: " $etext -ForegroundColor Green
#
# Decodificando contenido de un archivo
#
Write-Host "DECODIFICANDO el texto previo: "
[System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String($etext)) | Out-File -Encoding "ASCII" C:\Users\jorge\Desktop\Scripts07_1850014\secret.txt
$outfile12 = Get-Content C:\Users\jorge\Desktop\Scripts07_1850014\secret.txt
Write-Host "El texto decodificado es el siguiente: " -ForegroundColor Green
Write-Host "DECODIFICADO: " $outfile12