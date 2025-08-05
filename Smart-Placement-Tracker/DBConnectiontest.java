package tracker;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DBConnectiontest {
    public static void main(String[] args) {
        String url = "jdbc:mysql://localhost:3306/placement_tracker"; // Replace with your DB name
        String user = "root"; // Default MySQL user
        String password = "Jadhavasme1218@@"; // Default password (keep blank if using XAMPP with no password)

        try {
            Connection conn = DriverManager.getConnection(url, user, password);
            System.out.println("✅ Connection Successful!");
            conn.close();
        } catch (SQLException e) {
            System.out.println("❌ Connection Failed!");
            e.printStackTrace();
        }
    }
}
