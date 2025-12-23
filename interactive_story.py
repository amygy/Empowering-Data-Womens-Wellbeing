import pandas as pd

# Read India's electrification data
lwd = pd.read_csv("livwell135.csv")
india_data = lwd[lwd["country_name"] == "India"].sort_values("year")

print("-" * 70)
print("Households in rural areas with access to electricity")
print("-" * 70)
print()

# Story introduction
print("""
From 1993 to 2006, India embarked on one of the world's most ambitious 
journeys: bringing electricity to its rural villages. This isn't just about 
power lines and light bulbs it's about opportunity, hope, and especially 
women's empowerment.

Let's explore this story together!
""")

input("Press Enter to begin the journey through the 1990s...")
print()

# Extract all years data
years = india_data["year"].tolist()
rural_elec = india_data["ER_elec_rural_p"].tolist()
overall_elec = india_data["EI_elec_p"].tolist()
women_elec = india_data["EI_women_elec_p"].tolist()

print("The 1990s: The Starting Point")
print("-" * 70)
first_year = years[0]
first_rural = rural_elec[0]
first_overall = overall_elec[0]
first_women = women_elec[0]

print(f"""
In {first_year}, India faced a massive challenge:
  • Only {first_rural:.1f}% of rural households had electricity access
  • Overall, just {first_overall:.1f}% of people had any electrical connection
  • For women specifically, {first_women:.1f}% had access to electricity

This meant that over 500 million people, mostly in villages lived without 
electric lights, refrigeration, or communication tools. Women especially 
suffered, as without electricity:
  - No electric lights for studying or reading
  - No electric pumps for water access
  - No refrigeration to preserve food or medicine
  - Limited access to modern cooking methods
""")

input("Press Enter to see the government's plan...")
print()

print("""
The Mission: Rajiv Gandhi's Rural Electrification Scheme (1988) and later
National Power Policy aimed to bring electricity to every village by 2000.

Key Statistics from the Early Years:
""")

# Show year by year progression for first 5 years
for i in range(min(5, len(years))):
    print(f"  {years[i]}: Rural {rural_elec[i]:.1f}% | Overall {overall_elec[i]:.1f}% | Women {women_elec[i]:.1f}%")

input("Press Enter to see the mid-period challenges...")
print()

print("The Mid-Period (1998-2002): Progress with Challenges")
print("-" * 70)

mid_idx = len(years) // 2
print(f"""
By the early 2000s, the infrastructure was expanding rapidly:

  {years[mid_idx]}: Rural {rural_elec[mid_idx]:.1f}% | Overall {overall_elec[mid_idx]:.1f}% | Women {women_elec[mid_idx]:.1f}%

The good news: More villages were getting connected to the power grid.
The challenge: Creating the infrastructure was expensive and many areas 
still lacked reliable supply.
""")

input("Press Enter to hear the women's stories of change...")
print()

print("Women's Empowerment")
print("-" * 70)

# Calculate women's access improvement
women_improvement = women_elec[-1] - women_elec[0]
women_pct_gain = (women_improvement / women_elec[0]) * 100

print(f"""
One of the most remarkable aspects of electrification was its impact on women:

From {first_year} to {years[-1]}:
  • Women's electricity access grew from {women_elec[0]:.1f}% to {women_elec[-1]:.1f}%
  • That's an improvement of {women_improvement:.1f} percentage points
  • A {women_pct_gain:.1f}% relative increase!

With electricity, women could:
  - Read and study after dark
  - Use electric pumps to get water (instead of walking hours)
  - Refrigerate food and medicine
  - Listen to news and educational programs on radio
  - Watch television for information and entertainment
  - Feel safer with better lighting
""")

print("\n" + "=" * 70)
print("Thank you for exploring India's electrification story!")
print("=" * 70)
