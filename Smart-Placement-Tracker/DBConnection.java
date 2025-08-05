
package tracker;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DBConnection {
    public static Connection connect() throws SQLException {
        String url = "jdbc:mysql://localhost:3306/placement_tracker";
        String user = "root";      // your username
        String password = "Jadhavasme1218@@";      // your password (blank if using XAMPP)
        return DriverManager.getConnection(url, user, password);
    }
}
