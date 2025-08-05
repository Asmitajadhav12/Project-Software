package tracker;

public class CompanyAppTest {
    public static void main(String[] args) {
        Company c1 = new Company("Whizible Technologies", 7.5f);
        CompanyDAO dao = new CompanyDAO();
        dao.insertCompany(c1);
    }
}
