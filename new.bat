@echo off

set HR=%time:~0,2%
    
set HR=%Hr: =0% 
    
set HR=%HR: =%




cd C:\Program Files\Git\velu-repo\git-repo\velu
py -3 "new.py"
>>result.txt
pause
exit
