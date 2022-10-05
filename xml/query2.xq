for $x in doc("example.xml")/wechatContacts/contact
where $x/tag = "UT"
order by $x/tag
return $x/alias