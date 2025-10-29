# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "altair==5.5.0",
#     "marimo",
#     "pandas==2.3.3",
# ]
# ///

import marimo

__generated_with = "0.16.5"
app = marimo.App(
    width="full",
    app_title="wto-tariff-mfn",
    auto_download=["html"],
)


@app.cell
def _(box_chart, carousel, data, economies, intro, mo, products, summary_tab):
    mo.ui.tabs(
        {"Introduction":intro,
         "Data":data,
            "Viz - Reporting Economy": economies,
         "Viz - Product Categories":products,
         "Viz - Dispersion":box_chart,
         "Viz - Summary": summary_tab,
         "Insights":carousel
        }
    )
    return


@app.cell
def _(mo):
    mo.outline()
    return


@app.cell
def _(mo):
    mo.md(r"""#Dashboard Elements""")
    return


@app.cell
def _(mo):
    mfn_text = mo.md(
        f"""
    # 25 Years of Tariffs for the (current) Top 5 Reporting Economies
    ### **(China, European Union, India, Japan, United States of America)**

    I have analysed WTO data on annual simple average MFN tariffs on 22 product categories for the above five reporting economies for 2010 to 2024.

    - Which economies have higher tariffs than the others?
    - Have tariffs increased or decreased over time?
    - Which product categories have higher tariffs than the others?
    - Do tariffs vary widely over time, or do they remain at a steady level?
    - What are the interesting topics for further analysis?

    ## Most-Favored Nation Tariffs

    In current usage, MFN tariffs are what countries promise to impose on imports from other members of the WTO, unless the country is part of a preferential trade agreement (such as a free trade area or customs union). This means that, in practice, MFN rates are the highest (most restrictive) that WTO members charge one another.

        [Types of Tariffs from WITS](https://wits.worldbank.org/wits/wits/witshelp/content/data_retrieval/p/intro/c2.types_of_tariffs.htm)

    ## MTN Categories - Product Classification for WTO Trade Statistics

    The WTO's Multilateral Trade Negotiations (MTN) Categories is the product classification system used by the WTO for trade statistics and policy analysis. It allows the use of common terminology for interpreting trade trends and analysing policy measures, such as tariffs. The MTN categories, defined according to the Harmonised System, were recently reviewed and released as a new two-level structure comprising 22 MTN Categories and an additional 72 MTN sub-categories to provide more detailed information. 
    More information can be found on the WTO website [here](https://ttd.wto.org/en/news-blog/mtn-categories-product-classification-for-wto-trade-statistics-and-policy-analysis).

    **We will examine the tariff data for product groups at the MTN category level**
    The full list of categories can be found on pages 6-8 of this WTO [document](https://stats.wto.org/Areas/TimeSeries/src/assets/WTO_Multilateral_Trade_Negotiations_Categories_2023-06-26.pdf).

    ## Indicator: MFN - Simple Average Duty by Product Groups (percent)

    This data is downloaded from the WTO website as a CSV file and shows the simple average of the annual percentage duties imposed by the 5 largest world economies on imports of 22 different product categories, for the period 2010 to 2025. Here is the [link to download the data](https://ttd.wto.org/en/download/indicators).

    For an explanation of the calculation method of simple average of tariff line duties please refer to Page 3 of the [tariff aggregation method document by the WTO](https://www.wto.org/english/res_e/statis_e/wtp2006_special_topic_e.pdf).    
        """
    ).callout(kind='info')
    return (mfn_text,)


@app.cell
def _(mo):
    screenshot = mo.image(src="wto-data-screenshot.png",
             alt="Screenshot of data download page with the relevant search parameters",
             caption="Data Download Parameters")
    return (screenshot,)


@app.cell
def _(mo):
    df_text = mo.md(
        r"""
    # Dataset Used in the Visualisations
        """
    )
    return (df_text,)


@app.cell
def _(df, df_text, mfn_text, mo, screenshot):
    intro = mo.vstack([mfn_text, screenshot])
    data = mo.vstack([df_text, mo.ui.table(df)])
    return data, intro


@app.cell
def _(fig_region, mo, region):
    economies = mo.vstack([region, fig_region]) # dropdown for selecting reporting economy, followed by the associated heatmap chart
    return (economies,)


@app.cell
def _(category, fig_per, mo):
    products = mo.vstack([category, fig_per]) # Dropdown for selecting a product/sector, followed by updated line chart
    return (products,)


@app.cell
def _(mo):
    insights = mo.md(
        r"""
        # Insights

        ## India
        - India has the highest mean simple average tariff for 19 out of the 22 product categories in the period 2010 - 2024.

        - Out of the remaining three product categories, India comes second to Japan in 'Dairy products', was considerably higher than China in 'Cotton, silk and wool' for the years 2017 to 2022, and has been above China in 'Rubber, leather and footwear' since 2017.

        - India's tariffs have fluctuated more compared to the other reporting economies.

        - Tariffs for many product categories rose after 2017.
        """
    )
    return (insights,)


@app.cell
def _(mo):
    insights2 = mo.md(
        r"""
        # Insights
        ## Japan

        - Japan imposes much higher tariffs on dairy products compared to other product categories, with a significant jump after 2017.

        """
    )
    return (insights2,)


@app.cell
def _(mo):
    insights3 = mo.md(
        r"""
        # Insights
        ## China

        - China appears to focus on protecting its sugar industry.

        """
    )
    return (insights3,)


@app.cell
def _(mo):
    insights4 = mo.md(
        r"""
        # Insights
        ## European Union

        - The European Union imposes higher tariffs on dairy products compared to other product categories.

        """
    )
    return (insights4,)


@app.cell
def _(mo):
    insights5 = mo.md(
        r"""
        # Insights
        ## United States of America

        - The United States of America has the lowest tariffs in general among the five reporting economies.
        - Tariffs on dairy products are much higher compared to other product categories.

        """
    )
    return (insights5,)


@app.cell
def _(mo):
    next = mo.md(
        r"""
        # Next Steps

        - Re-run the analysis when 2025 data is available for all five reporting economies:
            * Are there matching increases or decreases between countries?
            * Is there a big difference from earlier years?
            * Obtain and analyse trade volume data to see if it is affected by changing tariffs.

        - Analyse tariff levels and trends for sub-categories to identify niches of interest.

        - Track tariff changes against foreign and domestic policies in the reporting economy.
        """
    )
    return (next,)


@app.cell
def _(high_chart, high_rep_chart, mean_chart, mo):
    summary_tab = mo.vstack([mean_chart,high_rep_chart,high_chart])
    return (summary_tab,)


@app.cell
def _(insights, insights2, insights3, insights4, insights5, mo, next):
    carousel = mo.carousel([
        mo.md("# 25 Years of Tariffs - Insights and Next Steps"),
        insights,
        insights2,
        insights3,
        insights4,
        insights5,
        next
    ])
    return (carousel,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Import Modules""")
    return


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import string
    import altair as alt
    return alt, mo, pd, string


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Data Loading and Processing""")
    return


@app.cell
def _(string):
    # MTN category codes are letters of the English alphabet from A to V
    mtn_codes = list(string.ascii_uppercase[:22]) #takes the first 22 letters (A through V)
    return (mtn_codes,)


@app.cell
def _(mo, mtn_codes, pd):
    @mo.cache
    def get_data():
        # Read the CSV file into a dataframe
        df = pd.read_csv('indicators_mfn_applied_duty_2010.csv').query("year != 2025") #dropping the year 2025 as India and the European Union do not have 2025 data
        # Select the desired columns
        columns_to_keep = ['reporter_name', 'year', 'product_code', 'mtn_categories', 'simple_average']
        new_df = df[columns_to_keep].sort_values(by=['reporter_name', 'mtn_categories', 'year'], 
                                                 ascending=[True, True, True])
        new_df = new_df[new_df['product_code'].isin(mtn_codes)]
        new_df = new_df.dropna(axis=0) #drop rows with NA values
        new_df['simple_average'] = new_df['simple_average'].round(1) #round to one decimal place
        return new_df
    return (get_data,)


@app.cell
def _(get_data):
    df = get_data()
    #df
    return (df,)


@app.cell
def _(df):
    mean_simple_average = df.groupby(['reporter_name', 'product_code', 'mtn_categories'])['simple_average'].mean().reset_index()
    mean_simple_average['simple_average'] = mean_simple_average['simple_average'].round(1)
    #mean_simple_average
    return (mean_simple_average,)


@app.cell
def _(mean_simple_average):
    # returns a dataframe of the reporting economy with the highest mean simple average tariff over 2010-2024 for each product category
    highest_per_mtn = mean_simple_average.loc[mean_simple_average.groupby('mtn_categories')['simple_average'].idxmax()]
    #highest_per_mtn
    return (highest_per_mtn,)


@app.cell
def _(mean_simple_average):
    # returns a dataframe of the product category with the highest mean simple average tariff over 2010-2024 for each reporting economy
    highest_per_reporter = mean_simple_average.loc[mean_simple_average.groupby('reporter_name')['simple_average'].idxmax()]
    #highest_per_reporter
    return (highest_per_reporter,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Charts""")
    return


@app.cell
def _(df, mo):
    # select a region to filter the data for that country/region
    region = mo.ui.dropdown(options=df["reporter_name"].unique().tolist(), value='United States of America', label='Reporting Economy')
    return (region,)


@app.cell
def _(alt, df, region):
    df_filter_region = df[df['reporter_name']==region.value]

    # Create the heatmap to show the duties for all product categories when a single reporting economy is selected
    fig_region = alt.Chart(df_filter_region).mark_rect().encode(
        x=alt.X("year:O", title=""),
        y=alt.Y("mtn_categories:N", title="Product Category"),
        color=alt.Color("simple_average:Q", scale=alt.Scale(scheme='plasma')),
        tooltip=["year", "mtn_categories", "simple_average"]
    ).properties(
        title=f"Simple Average MFN Tariff Duty % imposed by {region.value}"
    ).configure_axisX(
        labelAngle=0
    ).mark_text(baseline='middle').encode(
        alt.Text('simple_average:Q')
    ).properties(
        width="container",
        height=600)

    #fig_region
    return (fig_region,)


@app.cell
def _(df, mo):
    # Dropdown to select a product category
    category = mo.ui.dropdown.from_series(df['mtn_categories'], value='Chemicals', label='Product/Sector')
    return (category,)


@app.cell
def _(category, df):
    selection = (df['mtn_categories'] == category.value)
    return (selection,)


@app.cell
def _(alt, category, df, selection):
    # Create the line chart to show the duty for each selected product and each selection of regions over time

    # colour map for the economic countries/regions
    domain_ = ['China', 'European Union', 'India', 'Japan', 'United States of America']
    range_ = ['#DC143C', '#32CD32', '#FFA500', '#800080', '#1E90FF']

    fig_per = alt.Chart(df[selection]).mark_line(point=True).encode(
        x=alt.X("year:O", title="Year"),  # Ordinal scale if Year is categorical, Q if numerical
        y=alt.Y("simple_average:Q", title="MFN - Simple Avg Tariff Duty (%)"),
        color=alt.Color("reporter_name:N", legend=alt.Legend(orient="right")).scale(domain=domain_, range=range_),  # Horizontal legend
        tooltip=["year", "reporter_name", "simple_average"]
    ).properties(
        title=f"Simple Average Tariff Duty % for {category.value}",
        width="container",
        height=400
    ).configure_legend(
        direction="vertical",  # Make the legend vertical
    )
    #fig_per
    return domain_, fig_per, range_


@app.cell
def _(alt, domain_, mean_simple_average, range_):
    # replace _df with your data source
    mean_chart = (
        alt.Chart(mean_simple_average)
        .mark_point()
        .encode(
            x=alt.X(field='mtn_categories', type='nominal', title=None, axis=alt.Axis(# Set the angle of the axis labels here
            labelAngle=-45)),
            y=alt.Y(field='simple_average', type='quantitative', title=None),
            color=alt.Color(field='reporter_name', type='nominal', title=None).scale(domain=domain_, range=range_), # Add color encoding,
            tooltip=[
                alt.Tooltip(field='mtn_categories'),
                alt.Tooltip(field='simple_average', aggregate='mean', format=',.2f'),
                alt.Tooltip(field='reporter_name')
            ]
        )
        .properties(
            title='Mean of Simple Average MFN Tariff (%) for each Product Category over 2010 - 2024',
            width='container',
            config={
                'axis': {
                    'grid': False
                }
            }
        )
    )
    #mean_chart
    return (mean_chart,)


@app.cell
def _(alt, domain_, highest_per_mtn, range_):
    high_chart = alt.Chart(highest_per_mtn).mark_bar().encode(
        y=alt.Y('mtn_categories', sort='-x', title=None),
        x=alt.X('simple_average', title=None),
        color=alt.Color('reporter_name', title=None).scale(domain=domain_, range=range_), # Add color encoding
        tooltip=['mtn_categories', 'reporter_name', 'simple_average']
    ).properties(
        title='Highest Mean Simple Average Tariff (%) per MTN Category over 2010-2024',
        width="container"
    )
    #high_chart
    return (high_chart,)


@app.cell
def _(alt, df):
    box_chart = alt.Chart(df).mark_boxplot().encode(
        x=alt.X('mtn_categories:O', title='Product Category'), # Product categories on x-axis
        y=alt.Y('simple_average', title=None),
        row=alt.Row('reporter_name', title=None, header=alt.Header(labelOrient="left")), # Facet by row
        color=alt.Color('mtn_categories', legend=None), # Color by mtn_categories
        tooltip=['reporter_name', 'mtn_categories', 'simple_average']
    ).properties(
        title={'text':'Variability of Simple Average Tariff (%) by Reporting Economy and Product Category over 2010-2024', 'anchor':'middle'},
        width="container"
    )
    #box_chart
    return (box_chart,)


@app.cell
def _(alt, highest_per_reporter):
    # plot the chart for highest_per_reporter

    high_rep_chart = (
        alt.Chart(highest_per_reporter)
        .mark_bar()
        .encode(
            x=alt.X(field='simple_average', type='quantitative', title=None),
            y=alt.Y(field='reporter_name', type='nominal', title=None),
            color=alt.Color(field='mtn_categories', type='nominal', title=None).scale(scheme='accent'),
            tooltip=[
                alt.Tooltip(field='reporter_name'),
                alt.Tooltip(field='simple_average', aggregate='mean', format=',.2f'),
                alt.Tooltip(field='mtn_categories')
            ]
        )
        .properties(
            title='Highest Mean Simple Average Tariff (%) Product Category for each Reporting Economy over 2010-2024',
            width='container',
            config={
                'axis': {
                    'grid': False
                }
            }
        )
    )
    #high_rep_chart
    return (high_rep_chart,)


if __name__ == "__main__":
    app.run()
