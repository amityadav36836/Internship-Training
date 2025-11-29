import streamlit as st


movies = {
    "Avengers: Endgame": 10,
    "Inception": 8,
    "Titanic": 5
}


if "bookings" not in st.session_state:
    st.session_state.bookings = []

st.title("🎬 Movie Ticket Booking System")

st.header("Available Movies & Seats")
for movie, seats in movies.items():
    st.write(f"{movie} - Seats Available: {seats}")

st.header("Book Your Tickets")
movie_choice = st.selectbox("Select a movie", list(movies.keys()))
tickets = st.number_input("Number of tickets", min_value=1, step=1)

if st.button("Book Tickets"):
    if tickets <= movies[movie_choice]:
        movies[movie_choice] -= tickets
        ticket_id = len(st.session_state.bookings) + 1  # Incremental Ticket ID
        st.session_state.bookings.append({
            "movie": movie_choice,
            "tickets": tickets,
            "ticket_id": ticket_id
        })
        st.success(f"Booking Confirmed! \nMovie: {movie_choice}\nTickets: {tickets}\nTicket ID: {ticket_id}")
    else:
        st.error("Sorry, not enough seats available.")

st.header("Your Bookings")
if st.session_state.bookings:
    for b in st.session_state.bookings:
        st.write(f" Movie: {b['movie']} | Tickets: {b['tickets']} | Ticket ID: {b['ticket_id']}")
else:
    st.write("No bookings yet.")
