# --- QUICK FIX ---
# unreachable code
def foo():
  return 3
  foo()  
  pass 

# unnecessary, remove the else branch
if bla:
	foo()
	return 1
else:  
	return 2

# use snake_case not camelCase
def myFunction(arg1, arg2):
  pass



# --- Leave for examples in UI ---
# use snake_case not camelCase
def myOtherFunction():
  pass

# eval() can be unsafe
eval('[1, 2, 3]') 

# potential SQL injection
def add_product(db_connection, product: Product):
    cursor = db_connection.cursor()
    cursor.execute("INSERT INTO products (id, title) VALUES (NULL, '" + product.name+"');")
    db_connection.commit()
    import asyncio

# Unsanitized shell call.
def handler(event, context):
    # Should sanitize arguments
    async_loop.run_until_complete(async_loop.create_subprocess_shell("mycommand"))

    # Unsanitized shell call.
def handler(event, context):
    # Should sanitize arguments
    async_loop.run_until_complete(async_loop.create_subprocess_shell("mycommand"))