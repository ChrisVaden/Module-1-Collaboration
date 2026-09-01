#Chapter 3
seconds_per_hour = 60*60 #seconds per hour

seconds_per_day = 3600*60

total_divided = seconds_per_day / seconds_per_hour

print(seconds_per_hour, "Seconds Per hour")

print(seconds_per_day, " Seconds Per Day")


print(total_divided, "Seconds Divided")

#Chapter 4

song = """When an eel grabs your arm,... And it causes great harm,... That's - a moray!"""

song_capitalized = song.replace("moray", "moray".capitalize())
print("--- 4.1 ---")
print(song_capitalized)
print()

# ------------------------------------------------------------------------------
poem_template = """My kitty cat likes %s,
My kitty cat likes %s,
My kitty cat fell on his %s
And now thinks he's a %s."""

poem = poem_template % ("roast beef", "ham", "head", "clam")
print("--- 4.2 ---")
print(poem)
print()

letter = """Dear {salutation} {name},

Thank you for your letter. We are sorry that our {product}
{verbed} in your {room}. Please note that it should never
be used in a {room}, especially near any {animals}.

Send us your receipt and {amount} for shipping and handling.
We will send you another {product} that, in our tests,
is {percent}% less likely to have {verbed}.

Thank you for your support.

Sincerely,
{spokesman}
{job_title}"""

salutation = "Dr."
name = "Steaven Hawking"
product = "Sismec Dimensional Distrubitator"
verbed = "Decompressed"
room = "bedroom"
animals = "Pigeons"
amount = "$5.00"
percent = 99.9
spokesman = "Malakor Thunderpeck"
job_title = "Head of Customer Retaliations"

formatted_letter = letter.format(
    salutation=salutation,
    name=name,
    product=product,
    verbed=verbed,
    room=room,
    animals=animals,
    amount=amount,
    percent=percent,
    spokesman=spokesman,
    job_title=job_title,
)

print("--- 4.3 & 4.4 ---")
print(formatted_letter)
print()

print("--- 4.5 (%) ---")
print("Duck: %sy Mc%sface" % ("Ducky", "Duck"))
print("Gourd: %sy Mc%sface" % ("Gourdy", "Gourd"))
print("Spitz: %sy Mc%sface" % ("Spitzy", "Spitz"))
print()