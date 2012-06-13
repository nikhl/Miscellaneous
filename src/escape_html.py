def escape_html(s):
    if s:
        s = s.replace('&','&amp;')
        s = s.replace('<','&lt;')
        s = s.replace('>','&gt;')
        s = s.replace('"','&quot;')
        return s
    
    
print escape_html("> and > and < and < and & and & and \" and \" ")