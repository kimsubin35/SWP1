html = b"""
<html>
    <title> Operator </title>
    <body>
        <form action="">
            <em><FONT SIZE=5> Sum and Product of two number </FONT></em><br><br>
            number1 = <input type="number" name="number1"><br>
            number2 = <input type="number" name="number2"><br><br>
            <input type="submit" value="operator"><br>
        </form>
            (Sum) %(number1)d + %(number2)d = %(Sum)d<br>
            (Product) %(number1)d * %(number2)d = %(Product)d<br>
    </body>
</html>
"""
