import pandas as pd

# Read the data file
lwd = pd.read_csv("livwell135.csv")

# Get only India's data and sort by year
india_data = lwd[lwd["country_name"] == "India"].sort_values("year")

# Extract the columns we need
years = india_data["year"].tolist()
rural_elec = india_data["ER_elec_rural_p"].tolist()
women_elec = india_data["EI_women_elec_p"].tolist()

# Story title
print("=" * 60)
print("INDIA'S ELECTRICITY STORY (1993-2006)")
print("=" * 60)
print()

# Introduction
print("In 1993, most people in rural India had no electricity.")
print(f"Rural access: {rural_elec[0]:.1f}%")
print(f"Women's access: {women_elec[0]:.1f}%")
print()

input("Press Enter to see the progress...")
print()

# Show progress over time
print("Year-by-year progress:")
print("-" * 60)
print(f"{'Year':<8} {'Rural %':<15} {'Women %':<15}")
print("-" * 60)

for i in range(len(years)):
    print(f"{years[i]:<8} {rural_elec[i]:<15.1f} {women_elec[i]:<15.1f}")

print()
input("Press Enter to see what changed...")
print()

# Calculate changes
start_rural = rural_elec[0]
end_rural = rural_elec[-1]
start_women = women_elec[0]
end_women = women_elec[-1]

rural_change = end_rural - start_rural
women_change = end_women - start_women

# Show the results
print(f"From {years[0]} to {years[-1]}:")
print(f"  Rural electricity grew by {rural_change:.1f} percentage points")
print(f"  Women's access grew by {women_change:.1f} percentage points")
print()
print("This means:")
print(f"  • More villages got connected to power lines")
print(f"  • Women had better access to lights, fridges, and tools")
print(f"  • Families could study, work, and cook better")
print()

# Interactive part
user_year = input("Pick a year (1993-2006) to see details: ")

try:
    user_year = int(user_year)
    
    if user_year in years:
        idx = years.index(user_year)
        print()
        print(f"In {user_year}:")
        print(f"  Rural: {rural_elec[idx]:.1f}%")
        print(f"  Women: {women_elec[idx]:.1f}%")
    else:
        print(f"Year {user_year} not in data. Try a year between {years[0]} and {years[-1]}")
        
except:
    print("Please enter a valid year")

print()
print("=" * 60)
print("THE END")
print("=" * 60)
