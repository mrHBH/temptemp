import os
# html template : https://github.com/chhikaradi1993/Expandable-table-row
A=    """<!DOCTYPE html>
<html>

<head>
  <style>
    table {
      width: 100%;
      border: none;
      border-top: 1px solid #EEEEEE;
      font-family: arial, sans-serif;
      border-collapse: collapse;
    }

    td,
    th {
      border: 1px solid #EEEEEE;
      border-top: none;
      text-align: left;
      padding: 8px;
      color: #363D41;
      font-size: 14px;
    }

    tr {
      background-color: #fff;
      border: none;
      cursor: pointer;
      display: grid;
      grid-template-columns: repeat(1, 1fr);
      justify-content: flex-start;
    }

    tr:first-child:hover {
      cursor: default;
      background-color: #fff;
    }

    tr:hover {
      background-color: #EEF4FD;
    }

    .expanded-row-content {
      border-top: none;
      display: grid;
      grid-column: 1/-1;
      justify-content: flex-start;
      color: #AEB1B3;
      font-size: 13px;
      background-color: #fff;
    }

    .hide-row {
      display: none;
    }
  </style>
</head>

<body>
 <!--@Tag -->
  <script>
    const toggleRow = (element) => {
      element.getElementsByClassName('expanded-row-content')[0].classList.toggle('hide-row');
      console.log(event);
    }
  </script>

</body>

</html
"""
def GenerateTableHtml(dictionary,displayname):
    s = [' <h2> %s</h2>\n'% str(displayname)]
    for ECU in dictionary:             
        s.append('<table>\n <tr><th>%s</th></tr>\n' % str(ECU))
        for error in dictionary[ECU]:
            s.append('<tr onClick="toggleRow(this)">\n' )
            s.append('<td> %s</td>\n' % str(error))
            s.append('<td class="expanded-row-content hide-row">%s </td></tr>\n' % str(dictionary[ECU][error])) 
                    
        s.append('</table>\n')
    return '\n'.join(s)

template="<!--@Tag -->"

AddedErrorCodes= {'ECU12':{'Error54':"verw crir jqsd  dkljqsd  qsdlkjqsd  lkjqsd" ,'Error16':"3213 321 132 32132 xfd fxf132 "},'ECU166':{'error455':"4544554456654654 546546 456645"}} 
AddedErrorCodes= {'ECU12éééé':{'Error54':"veqds crir jqsd  dkljqsd  qsdlkjqsd  lkjqsd" ,'Error16':"3213 321 132 32132 xfd fxf132 "},'ECU166':{'error455':"4544554456654654 546546 456645"}} 





q=GenerateTableHtml(AddedErrorCodes,"blocA") + "\n" + GenerateTableHtml(AddedErrorCodes,"blocB")

B=A.replace(template,q)

text_file = open("Output.html", "w")
text_file.write(B)
text_file.close()
os.startfile("Output.html")
print(B)



