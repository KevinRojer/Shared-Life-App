from fpdf import FPDF

class ReportGenerator:
    """
    Handles the creation of PDF reports.
    """

    def __init__(self, report_name):
        self.report_name = report_name


    def generate_pdf(self, flatmates, bill):
        """
        Generates a PDF report stating the names of the flatmates, 
        the period, and how much they have to pay.
        """
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, f"Bill Period: {bill.period}", 0, 1)
        pdf.cell(0, 10, f"Total Bill Amount: ${bill.amount}", 0, 1)
        pdf.cell(0, 10, "Details:", 0, 1)

        total_days = sum([flatmate.days_in_house for flatmate in flatmates])
        for flatmate in flatmates:
            share = flatmate.pay_share(bill, total_days)
            pdf.cell(0, 10, f"{flatmate.name}: ${share:.2f}", 0, 1)

        pdf.output(self.report_name)