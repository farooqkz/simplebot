#!/usr/bin/perl -w

use IO::Socket;

my $PORT = 6667;
my $HOST = "irc.freenode.net";
my $NICK = "simplebot";

my $sock = new IO::Socket::INET(PeerAddr=>$HOST, PeerPort=>$PORT, Proto=>'tcp');
print $sock "USER ".(($NICK." ") x 3).":".$NICK."\r\n"."NICK ".$NICK."\r\n";
print $sock "JOIN ##temp\r\nPRIVMSG ##temp :Hi!\r\n";
while ($line = <$sock>){
    $_ = $line;
    if (m/^PING/){
        s/^PING //;
        print $sock;
    }
}
