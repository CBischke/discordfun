from opendota.connection import Connection

con = Connection()
sql = "select%20%2A%20from%20public_matches%20where%20avg_mmr%20%3E%203000%20and%20game_mode%20%3D%2022%20order%20by%20start_time%20desc%20limit%201000"
print(con.getLatestMatches())
