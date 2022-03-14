<html>
<body>
<table>
% for item in shopping_list:
   <tr>
      <td>{{item['id']}}</td>
      <td>{{item['desc']}}</td>
      <td><a href="/Edit/{{item['id']}}">Edit</a></td>
   </tr>
%  end

<hr/>
</table>
<a href='/edit_item'>Add an Item...</a>
</body>
</html>