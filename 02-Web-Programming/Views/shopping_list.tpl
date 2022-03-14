<html>
<body>
<table>
% for item in shopping_list:
   <tr>
      <td>{{item['id']}}</td>
      <td>{{item['desc']}}</td>
      <td><a href="/delete/{{item['id']}}">Delete</a></td>
   </tr>
%  end

<hr/>
</table>
<a href='/Add'>Add an Item...</a>
</body>
</html>