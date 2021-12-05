<html>
<head>
</head>
<body>
	<h1>Fibonacci</h1>
<%!
	public String fibonacci(String parameter)
	{
		int c = 1;
        int a = 0;
        int b = 1;
        for (int i = 2; i <= Integer.parseInt(parameter); i++) 
        {
            c = a + b;
            a = b;
            b = c;
        }
		return c+"";
	};
%>
<% out.print(fibonacci(request.getParameter("numero").toString())); %>


</body>

</html>