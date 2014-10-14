#!/usr/bin/perl

use warnings;
use strict;
use Browser::Open qw( open_browser );

my $url = 'https://www.youtube.com/watch?v=LpOwzzQyK70';

if (true) {
        sleep(4*60*50);
        open_browser($url);
}