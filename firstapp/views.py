from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def greeting(request):
    return HttpResponse('hello all, welcome to our web development class')
def student(request):
    return HttpResponse('''
<h1>StudentName : Sailaja</h1>
                        <i>Education : Bachelore of Computer Science</i>
                        <h3><b>CGP : 8.2</b></h3>
                        <marquee>CollegeName: Sree Venkateswara Degree College</marquee>
                        <img src="https://i.ytimg.com/vi/J-YS9lLVnLg/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLBB0xxeZUlH8v07XdWUARLOEKx1hA" width="500px" align="center">
''')
def festival(request):
    return HttpResponse('''<h1 style="background-color:DodgerBlue;"><i>happy christmas to all my friends!!!</i></h1>
                        <img src="https://cdn.pixabay.com/photo/2023/12/15/01/09/christmas-8449873_640.png" style="float:left;width=10px;height=25px">
                        ''')
def rigform(request):
    return HttpResponse('''
<form>
                        <label for="fname">First name:</label><br>
                        <input type="text" id="fname" name="fname"><br>
                        <label for="lname">Last name:</label><br>
                        <input type="text" id="lname" name="lname">
                        </form>
                        ''')

def table(request):
    return HttpResponse('''<table>
  <tr>
    <th>Company</th>
    <th>Contact</th>
    <th>Country</th>
  </tr>
  <tr>
    <td>Alfreds Futterkiste</td>
    <td>Maria Anders</td>
    <td>Germany</td>
  </tr>
  <tr>
    <td>Centro comercial Moctezuma</td>
    <td>Francisco Chang</td>
    <td>Mexico</td>
  </tr>
</table>''')

def bgimg(request):
    return HttpResponse('''
                        <p><h3 style="color:red;">Background image style</h3></p>
                        <p style="background-image:url('sea.jpg');float:right;color:white;">The lorem tag inserts a specified amount of random text. The "random" text is the famous "Lorum ipsum" text, in lower case letters.What is Lorem Ipsum?
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

Why do we use it?
It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).


Where does it come from?
Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.

The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.

Where can I get some?
There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.

5
	paragraphs
	words
	bytes
	lists
	Start with 'Lorem
ipsum dolor sit amet...'
</p>''')
