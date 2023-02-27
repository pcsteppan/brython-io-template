from browser import document, html

# a function which takes an 'event', which is data associated with the user's button click
def greet(event):
    # 'Prevent default' is a weird one. Typically when a user submits a 'form', the browser has to redirect or refresh to show
    # new data from the server. In our case though, we aren't calling a server at all, so this 'prevents' the 'default' behavior of refreshing.
    event.preventDefault()

    # this grabs the 'main-input' element from our HTML, and then grabs its value, and stores it in input
    input = document["main-input"].value

    # this clears out the previous output
    document["main-output"].clear()

    # and this writes our new output to the HTML
    # the weird '<=' arrow is Brython's way of creating a new HTML element and putting it inside of another HTML element.
    # in this case, we're creating a new string element, and putting it inside the 'main-output' element in the HTML.
    document["main-output"] <= (f"Hello, {input}")

# This creates a link between our function 'greet' seen above, and the form in the HTML
# It says, when the 'main-form' in out HTML is 'sumbit'ed, execute the greet function
document["main-form"].bind("submit", greet)

# This prints 'hello' to the browser's console, you can often open that up with ctrl+shift+c, or by inspecting the page with right-click.
# Then find 'Console' tab, and you can see the output there 
print('hello')