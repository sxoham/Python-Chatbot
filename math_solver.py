import math
import re

def sin_deg(x): return math.sin(math.radians(x))
def cos_deg(x): return math.cos(math.radians(x))
def tan_deg(x): return math.tan(math.radians(x))

allowed_names = {
    "sqrt": math.sqrt,
    "sin": sin_deg,
    "cos": cos_deg,
    "tan": tan_deg,
    "log": math.log,
    "pi": math.pi,
    "e": math.e,
    "pow": pow,
    "__builtins__": None 
}

def safe_eval(expr):
    try:
        expr = expr.replace("^", "**")
        expr = re.sub(r"[^0-9a-zA-Z+*/().,\s-]", "", expr)  # Clean unsafe chars
        result = eval(expr, {"__builtins__": None}, allowed_names)
        return f"The answer is {round(result, 6)}"
    except Exception as e:
        return " Sorry, I couldn't solve that. Make sure it's a valid math expression."
