import pandas as pd

# Read India's electrification data
lwd = pd.read_csv("livwell135.csv")
india_data = lwd[lwd["country_name"] == "India"].sort_values("year")

print("=" * 70)
print("THE LIGHT OF PROGRESS: India's Journey to Rural Electrification")
print("=" * 70)
print()

# Story introduction
print("""
Welcome to India's incredible transformation story. From 1993 to 2006, India 
embarked on one of the world's most ambitious journeys: bringing electricity 
to its rural villages. This isn't just about power lines and light bulbs—
it's about opportunity, hope, and especially women's empowerment.

Let's explore this story together...
""")

input("Press Enter to begin the journey through the 1990s...")
print()

# Extract all years data
years = india_data["year"].tolist()
rural_elec = india_data["ER_elec_rural_p"].tolist()
overall_elec = india_data["EI_elec_p"].tolist()
women_elec = india_data["EI_women_elec_p"].tolist()

print("🏘️  THE 1990s: THE STARTING POINT")
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

This meant that over 500 million people—mostly in villages—lived without 
electric lights, refrigeration, or communication tools. Women especially 
suffered, as without electricity:
  - No electric lights for studying or reading
  - No electric pumps for water access
  - No refrigeration to preserve food or medicine
  - Limited access to modern cooking methods
""")

input("Press Enter to see the government's ambitious plan...")
print()

print("""
🎯 THE MISSION: Rajiv Gandhi's Rural Electrification Scheme (1988) and later
National Power Policy aimed to bring electricity to every village by 2000.

Key Statistics from the Early Years:
""")

# Show year-by-year progression for first 5 years
for i in range(min(5, len(years))):
    print(f"  {years[i]}: Rural {rural_elec[i]:.1f}% | Overall {overall_elec[i]:.1f}% | Women {women_elec[i]:.1f}%")

input("Press Enter to see the mid-period challenges...")
print()

print("📊 THE MID-PERIOD (1998-2002): Progress with Challenges")
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

print("👩 WOMEN'S EMPOWERMENT: The Hidden Victory")
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
  ✓ Read and study after dark
  ✓ Use electric pumps to get water (instead of walking hours)
  ✓ Refrigerate food and medicine
  ✓ Listen to news and educational programs on radio
  ✓ Watch television for information and entertainment
  ✓ Work from home (some industries moved to villages)
  ✓ Feel safer with better lighting
""")

input("Press Enter for the final victory...")
print()

print("🌟 THE TRIUMPH (2006): A New Era")
print("-" * 70)

last_year = years[-1]
last_rural = rural_elec[-1]
last_overall = overall_elec[-1]
last_women = women_elec[-1]

print(f"""
By {last_year}, the dream was becoming reality:

  • {last_rural:.1f}% of rural households had electricity (up from {first_rural:.1f}%)
  • Overall electrification: {last_overall:.1f}% (from {first_overall:.1f}%)
  • Women's access: {last_women:.1f}% (from {first_women:.1f}%)

Overall Rural Improvement: +{last_rural - first_rural:.1f} percentage points
Women's Improvement: +{last_women - first_women:.1f} percentage points
""")

input("Press Enter to see the real-world impact...")
print()

print("💡 WHAT THIS MEANT IN REAL LIVES")
print("-" * 70)

households_affected = 400_000_000  # Approximate rural population

print(f"""
These percentages represent millions of lives changed:

Estimated rural households in India: ~{households_affected/1_000_000:.0f} million

In {first_year}:
  • Households WITH electricity: ~{(first_rural/100) * households_affected/1_000_000:.0f} million
  • Households WITHOUT electricity: ~{((100-first_rural)/100) * households_affected/1_000_000:.0f} million

By {last_year}:
  • Households WITH electricity: ~{(last_rural/100) * households_affected/1_000_000:.0f} million
  • Households WITHOUT electricity: ~{((100-last_rural)/100) * households_affected/1_000_000:.0f} million

That's approximately {((last_rural-first_rural)/100) * households_affected/1_000_000:.0f} million additional households 
gaining access to electricity!
""")

input("Press Enter to see the year-by-year complete data...")
print()

print("📈 COMPLETE DATA JOURNEY: {}-{}".format(years[0], years[-1]))
print("-" * 70)
print(f"{'Year':<8} {'Rural %':<12} {'Overall %':<12} {'Women %':<12} {'Change':<15}")
print("-" * 70)

for i in range(len(years)):
    if i == 0:
        change = "Starting point"
    else:
        change = f"+{women_elec[i] - women_elec[i-1]:.1f}pp"
    
    print(f"{years[i]:<8} {rural_elec[i]:<12.1f} {overall_elec[i]:<12.1f} {women_elec[i]:<12.1f} {change:<15}")

print()
input("Press Enter for the conclusion...")
print()

print("✨ THE LEGACY")
print("-" * 70)

avg_annual_growth = (last_women - first_women) / len(years)

print(f"""
From {first_year} to {last_year}:

India demonstrated that with determination, millions of lives can be 
transformed through infrastructure development.

Key Takeaways:
  1. Women's electrification grew faster than overall rates, showing 
     prioritization of gender equality
  2. Rural areas lagged behind overall average, but the gap was closing
  3. The trajectory shows sustainable, steady progress year after year
  4. Average annual improvement for women: +{avg_annual_growth:.2f} percentage points/year

This story isn't just about electricity—it's about:
  • Healthcare (refrigeration for medicine)
  • Education (reading and learning tools)
  • Safety (lighting)
  • Economic opportunity (small business and industry)
  • Gender equality (women's autonomy and power)

Today, the journey continues. India still works to reach 100% 
electrification and ensure reliable, sustainable power for all.
""")

user_input = input("\nWould you like to explore any specific year in detail? (Enter year or 'no'): ")

if user_input.lower() != 'no':
    try:
        target_year = int(user_input)
        if target_year in years:
            idx = years.index(target_year)
            print(f"\n📊 DETAILED VIEW FOR {target_year}")
            print("-" * 70)
            print(f"Rural Electrification: {rural_elec[idx]:.1f}%")
            print(f"Overall Electrification: {overall_elec[idx]:.1f}%")
            print(f"Women's Electrification: {women_elec[idx]:.1f}%")
            
            if idx > 0:
                print(f"\nYear-over-year changes:")
                print(f"  Rural: {rural_elec[idx] - rural_elec[idx-1]:+.1f}pp")
                print(f"  Overall: {overall_elec[idx] - overall_elec[idx-1]:+.1f}pp")
                print(f"  Women: {women_elec[idx] - women_elec[idx-1]:+.1f}pp")
        else:
            print(f"Data not available for {target_year}. Available years: {years}")
    except ValueError:
        print("Invalid input.")

print("\n" + "=" * 70)
print("Thank you for exploring India's electrification story!")
print("=" * 70)
