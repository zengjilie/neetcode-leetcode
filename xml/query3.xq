for $x in doc("example.xml")/wechatContacts/contact
where $x/tag = "UT" or $x/tag = "UT MSIS" 
order by $x/tag
return <li>{data($x/alias)}</li>
