$apturetie = Get-Service |
	Where-Object { $_.Status -eq "Stopped" } |
	Sort-Object Name |
	Select-Object Name, Status

$aptretie | Export-Csv -Path "apturetie.csv" -NoTypeInformation -Encoding utf8
Write-Host "Fails gatavs"