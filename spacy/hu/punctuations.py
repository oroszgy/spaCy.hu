# encoding: utf8
from __future__ import unicode_literals

TOKENIZER_PREFIXES = r'''
,
"
(
)
[
{
*
<
>
¡
¿
!
?
„
“
'
``
`
#
‘
....
...
…
‚
»
US$
C$
A$
'''.strip().split('\n')

TOKENIZER_SUFFIXES = r'''
,
\"
(?<=[^0-9])[)\]}]
\*
\!
\?
>
:
;
'
”
“
«
_
''
’
‘
´
…
\-\-
\.\.
\.\.\.
\.\.\.\.
(?<=[a-züóőúéáűí\]"'´«‘’%\)²“”+\-])\.
(?<=[a-züóőúéáűí!?.]["'´«»‘’%\)²“”])-[a-züóőúéáűí]+
(?<=[$€¢%§%])\.
(?<=[a-züóőúéáűí)])-e
(?<=°[FCK])\.
(?<=[0-9])[+\-/*]
'''.strip().split('\n')

TOKENIZER_INFIXES = r'''
…
\.\.+
(?<=[a-züóőúéáűí])\.(?=[A-ZÜÓŐÚÉÁŰÍ])
(?<=[a-zA-ZüóőúéáűíÜÓŐÚÉÁŰÍ0-9])"(?=[\-a-zA-ZüóőúéáűíÜÓŐÚÉÁŰÍ])
(?<=[a-zA-ZüóőúéáűíÜÓŐÚÉÁŰÍ])--(?=[a-zA-ZüóőúéáűíÜÓŐÚÉÁŰÍ])
(?<=[a-zA-ZüóőúéáűíÜÓŐÚÉÁŰÍ]),(?=[a-zA-ZüóőúéáűíÜÓŐÚÉÁŰÍ])
'''.strip().split('\n')

__all__ = ["TOKENIZER_PREFIXES", "TOKENIZER_SUFFIXES", "TOKENIZER_INFIXES"]
