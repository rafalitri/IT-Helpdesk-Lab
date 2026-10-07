Write-Host "=== DIAGNOSTICO WINDOWS ==="


# ==========================================
# INFORMACION DEL EQUIPO
# ==========================================

Write-Host ""
Write-Host "Nombre del equipo:"
Write-Host $env:COMPUTERNAME


# ==========================================
# SISTEMA OPERATIVO
# ==========================================

try {
    $os = Get-CimInstance Win32_OperatingSystem -ErrorAction Stop
}
catch {
    Write-Host "ERROR: No se pudo obtener informacion del sistema operativo."
    exit 1
}

Write-Host ""
Write-Host "=== SISTEMA OPERATIVO ==="
Write-Host "Sistema:" $os.Caption
Write-Host "Version:" $os.Version
Write-Host "Arquitectura:" $os.OSArchitecture


# ==========================================
# MEMORIA RAM
# ==========================================

Write-Host ""
Write-Host "=== MEMORIA RAM ==="

$totalRAM = [math]::Round(
    ($os.TotalVisibleMemorySize * 1KB) / 1GB,
    2
)

$libreRAM = [math]::Round(
    ($os.FreePhysicalMemory * 1KB) / 1GB,
    2
)

$usadaRAM = [math]::Round(
    $totalRAM - $libreRAM,
    2
)

if ($totalRAM -gt 0) {
    $porcentajeRAM = [math]::Round(
        ($usadaRAM / $totalRAM) * 100,
        2
    )
}
else {
    $porcentajeRAM = 0
}

Write-Host "RAM total:" $totalRAM "GB"
Write-Host "RAM usada:" $usadaRAM "GB"
Write-Host "RAM libre:" $libreRAM "GB"
Write-Host "Uso de RAM:" $porcentajeRAM "%"

if ($porcentajeRAM -gt 85) {
    Write-Host "ADVERTENCIA: Uso elevado de memoria RAM"
}
else {
    Write-Host "Estado de RAM: Correcto"
}


# ==========================================
# DISCOS
# ==========================================

Write-Host ""
Write-Host "=== DISCOS ==="

try {
    $discos = Get-CimInstance Win32_LogicalDisk `
        -Filter "DriveType=3" `
        -ErrorAction Stop

    foreach ($disco in $discos) {

        # Ignorar unidades menores de 1 GB
        if (-not $disco.Size -or $disco.Size -lt 1GB) {
            continue
        }

        $total = [math]::Round(
            $disco.Size / 1GB,
            2
        )

        $libre = [math]::Round(
            $disco.FreeSpace / 1GB,
            2
        )

        $usado = [math]::Round(
            $total - $libre,
            2
        )

        $porcentajeLibre = [math]::Round(
            ($libre / $total) * 100,
            2
        )

        Write-Host ""
        Write-Host "Disco:" $disco.DeviceID
        Write-Host "Espacio total:" $total "GB"
        Write-Host "Espacio usado:" $usado "GB"
        Write-Host "Espacio libre:" $libre "GB"
        Write-Host "Porcentaje libre:" $porcentajeLibre "%"

        if ($porcentajeLibre -lt 15) {
            Write-Host "ADVERTENCIA: Poco espacio libre en el disco"
        }
        else {
            Write-Host "Estado del disco: Correcto"
        }
    }
}
catch {
    Write-Host "ERROR: No se pudo obtener informacion de los discos."
}


# ==========================================
# PROCESOS CON MAYOR USO DE RAM
# ==========================================

Write-Host ""
Write-Host "=== PROCESOS CON MAYOR USO DE RAM ==="

$procesos = Get-Process -ErrorAction SilentlyContinue |
    Sort-Object WorkingSet64 -Descending |
    Select-Object -First 5

if ($procesos) {

    foreach ($proceso in $procesos) {

        $ramMB = [math]::Round(
            $proceso.WorkingSet64 / 1MB,
            2
        )

        Write-Host "Proceso:" $proceso.Name
        Write-Host "PID:" $proceso.Id
        Write-Host "RAM:" $ramMB "MB"
        Write-Host ""
    }
}
else {
    Write-Host "No se pudo obtener informacion de los procesos."
}


# ==========================================
# CONFIGURACION DE RED
# ==========================================

Write-Host ""
Write-Host "=== CONFIGURACION DE RED ==="

try {
    $configuraciones = Get-NetIPConfiguration -ErrorAction Stop |
        Where-Object {
            $_.IPv4Address -ne $null
        }

    if (-not $configuraciones) {
        Write-Host "No se encontraron adaptadores con IPv4."
    }

    foreach ($config in $configuraciones) {

        Write-Host ""
        Write-Host "Adaptador:" $config.InterfaceAlias

        $ipv4 = $config.IPv4Address.IPAddress -join ", "
        Write-Host "IPv4:" $ipv4

        if ($config.IPv4DefaultGateway) {
            Write-Host "Puerta de enlace:" $config.IPv4DefaultGateway.NextHop
        }
        else {
            Write-Host "Puerta de enlace: No disponible"
        }

        $dns = Get-DnsClientServerAddress `
            -InterfaceIndex $config.InterfaceIndex `
            -AddressFamily IPv4 `
            -ErrorAction SilentlyContinue

        if ($dns.ServerAddresses) {
            Write-Host "DNS:" ($dns.ServerAddresses -join ", ")
        }
        else {
            Write-Host "DNS: No disponible"
        }
    }
}
catch {
    Write-Host "ERROR: No se pudo obtener la configuracion de red."
}


# ==========================================
# SERVICIOS IMPORTANTES
# ==========================================

Write-Host ""
Write-Host "=== SERVICIOS IMPORTANTES ==="

$servicios = @(
    "Dhcp",
    "Dnscache"
)

foreach ($nombreServicio in $servicios) {

    $servicio = Get-Service `
        -Name $nombreServicio `
        -ErrorAction SilentlyContinue

    if ($servicio) {

        Write-Host ""
        Write-Host "Servicio:" $servicio.DisplayName
        Write-Host "Nombre:" $servicio.Name
        Write-Host "Estado:" $servicio.Status

        if ($servicio.Status -eq "Running") {
            Write-Host "Estado del servicio: Correcto"
        }
        else {
            Write-Host "ADVERTENCIA: El servicio no esta ejecutandose"
        }
    }
    else {
        Write-Host ""
        Write-Host "No se encontro el servicio:" $nombreServicio
    }
}


Write-Host ""
Write-Host "=== FIN DEL DIAGNOSTICO ==="