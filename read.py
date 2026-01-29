import pandas as pd

df = pd.read_csv("data.csv")

output = []
output.append(f"Shape: {df.shape}\n")
output.append("First 5 rows:\n")
output.append(df.head().to_string())

result = "\n".join(output)

print(result)

# DVC output
with open("output.txt", "w") as f:
    f.write(result)

