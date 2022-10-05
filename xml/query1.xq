for $x in doc("example.xml")/wechatContacts/contact
order by $x/tag
return $x/tag