
\c testfligoo;

-- Create the table
CREATE TABLE IF NOT EXISTS testdata (
    flight_id SERIAL PRIMARY KEY,
    flight_date DATE,
    flight_status VARCHAR(10),
    departure_airport VARCHAR(255),
    departure_timezone VARCHAR(255),
    arrival_airport VARCHAR(255),
    arrival_timezone VARCHAR(255),
    arrival_terminal VARCHAR(10),
    airline_name VARCHAR(255),
    flight_number INT
);
