import streamlit as st
import pandas as pd
import datetime

# Layout setting of the page
st.set_page_config(layout="centered")

# initialize list elements
family = ["Opa", "Oma", "Günter", "Karin", "Kirsten", "Henrik","Rebecca" ,"Simone", "Bernd", "Timon", "Dorian", "Kristina", "Frederik", "Ann-Sophie", "Aurelie", "Matthis"]
anzahl = [0,1,2,3,4,5]  

# Create the pandas DataFrame with column name is provided explicitly
df_family = pd.DataFrame(family, columns=['Name'])

# Add Columns
df_family["Anzahl Paprikawurst"] = 0
df_family["Anzahl Käseknacker"] = 0 
df_family["Bringt mit"] = "Nichts"
df_family["Eingetragen am"] = "Abfrage nicht ausgefüllt"

# Header
st.markdown("<h1 style='text-align: center; color: black;'>Willkommen auf dem Abfrage-Tool für Familie Pitz</h1>", unsafe_allow_html=True)
st.markdown("<hr/>", unsafe_allow_html=True)

# Abfrage
st.subheader("Gib hier deine Wünsche an:")

with st.form(key = "columns in form"):
    # Subheader Name
    st.write("Wähle bitte deinen Name aus")
    family_list = ["Name", "Opa", "Oma", "Günter", "Karin", "Kirsten", "Henrik","Rebecca" ,"Simone", "Bernd", "Timon", "Dorian", "Kristina", "Frederik", "Ann-Sophie", "Aurelie", "Matthis"]
    name = st.selectbox("Mein Name lautet", family_list)

    # Subheader Paprikawurst
    st.write("Wie viele Paprikawürste willst du esssen?")
    value_paprika = st.slider("Anzahl Würste", 0,5,0, key = 1)

    # Subheader Käseknacker
    st.write("Wie viele Käseknacker willst du essen?")
    value_käse = st.slider("Anzahl Würste", 0,5,0, key = 2)

    # Subheader Mitbringsel
    st.write("Was bringst du für das Fest mit? (Salat, Kuchen...)")
    Mitbringsel = st.text_input('Ich bringe mit...', "Nichts")

    if name != "Name":
        #Update of the dataframe
        df_family.loc[df_family.Name == name, "Anzahl Paprikawurst"] = value_paprika
        df_family.loc[df_family.Name == name, "Anzahl Käseknacker"] = value_käse
        df_family.loc[df_family.Name == name, "Bringt mit"] = Mitbringsel
        df_family.loc[df_family.Name == name, "Eingetragen am"] = str(datetime.datetime.now())

    submitted = st.form_submit_button("Abschicken")

# Conclusion of the request
st.subheader("Ergebnis der Abfrage:")
st.write("Summe Paprikawürste: " + str(sum(df_family["Anzahl Paprikawurst"])))
st.write("Summe Käseknacker: " + str(sum(df_family["Anzahl Käseknacker"])))

# show dataframe.
st.table(df_family)

# Reset the table
st.markdown("<hr/>", unsafe_allow_html=True)

with st.form(key = "reset"):

    # Add Columns
    df_family["Anzahl Paprikawurst"] = 0
    df_family["Anzahl Käseknacker"] = 0 
    df_family["Bringt mit"] = "Nichts"
    df_family["Eingetragen am"] = "Abfrage nicht ausgefüllt"

    submitted = st.form_submit_button("Zurücksetzen der Abfrage")

