``` bash
uvicorn 3-1_hello:app --reload

http  -v POST localhost:8000/hello who=mom

http  -v POST localhost:8000/hello who:mom
```

FastAPI converts HTTP header keys to lowercase, and converts a hyphen (-) to an
underscore (_).


Threads are often recommended when your program is I/O bound, and multiple pro‐
cesses are recommended when you’re CPU bound.


model validation solutions
Dataclass attrs Pydantic marsh-mallow Voluptuous

defining dependencies to separate specific details from
your general code

In FastAPI, a dependency is something that’s executed, so a dependency object needs
to be of the type Callable, which includes functions and classes—things that you
call, with parentheses and optional arguments.


鉴权的方式:
username/email password 
    classic http basic and digest authentication
API key (applying to external program)
    an opaque long string with an accompanying secret
Oauth2
    a set of standards for authentication and authorization
JWT
    an encoding format containing cryptographically signed user information


http -a me:secret  -v localhost:8000/who







