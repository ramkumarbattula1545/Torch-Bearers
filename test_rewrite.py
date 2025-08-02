from rewrite import rewrite_text   # import your modified rewrite_text function

input_text = "Your original text here."
rewrites = rewrite_text(input_text)

print("Suspenseful version:")
print(rewrites["suspenseful"])

print("\nNeutral version:")
print(rewrites["neutral"])

print("\nProfessional version:")
print(rewrites["professional"])
