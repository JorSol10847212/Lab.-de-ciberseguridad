#Escaneo de equipos activos en la subred
#
# Determinado gateway
$subred = (Get-NetRoute -DestinationPrefix 0.0.0.0/0).NextHop
Write-Host "== Determinando tu gateway ..."
Write-Host "Tu gateway: $subred"

#
# Determinando rango de subred
#
$rango = $subred.Substring(0,$subred.IndexOf(".") + 1 + $subred.Substring($subred.IndexOf(".") + 1).IndexOf(".") + 3)
Write-Host "== Determinando tu rango de subred ..."
echo $rango

#
## Determinando si $rango termina en "."
## En ocasiones el rango de subred no termina en punto, necesitamos formarlo.
#
$punto = $rango.EndsWith(".")
if ( $punto -like "False" )
{
	$rango = $rango + "." #agregamos el punto en caso de que no estuvieran
}

#
## Creamos un array con puertos a escanear
## Establecemos una variable para Waittime
#
$portstoscan = @(20,21,22,23,25,50,51,53,80,110,119,135,136,137,138,139,143,161,162,389,443,445,636,1025,1443,3389,5985,5986,8080,10000)
$waittime = 100

#
## Solicitamos dirección ip a escanear:
#
Write-Host "Dirección ip a escanear: " -NoNewline
$direccion = Read-Host

#
##Generamos bucle foreach para evaluar cada puerto en $portstoscan
#
foreach ( $pin in $portstoscan )
{
	$TCPObject = new-object System.Net.Sockets.TcpClient
		try{ $resultado = $TCPObject.ConnectAsync($direccion,$p).Wait($waittime)}catch{}
		if ( $resultado -eq "True")
		{
			Write-Host "Puerto abierto: " -NoNewline; Write-Host $p -ForegroundColor Green
		}
}
	
