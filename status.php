<?php
  $server = "minecraft.flipdot.org";
  $port = "25565";
  $timeout = 10;
  if ($server and $port and $timeout) 
  {
    $serverstatus = @fsockopen("$server", $port, $errno, $errstr, $timeout);
  }
  if($serverstatus) 
  {
    echo "Alles bestens =)";  
  }
  else 
  {
    echo "Sorry, Server ist offline =(";
  }
?>
