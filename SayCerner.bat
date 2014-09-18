@echo off
@echo set s = CreateObject("SAPI.SpVoice")> cernereng.vbs
@echo s.Speak Wscript.Arguments(0), 3 >> cernereng.vbs
@echo s.WaitUntilDone(10000)>> cernereng.vbs
cscript cernereng.vbs "I write blogs, participate in hack nights and trivia nights, attend meetups and conferences and share  knowledge. Oh yea, I am a Sir ner engineer."
del "cernereng.vbs"
 