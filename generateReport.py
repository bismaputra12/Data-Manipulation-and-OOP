class Report:
    def __init__(self, ID, UNSPSC, Price):
        self.ID = ID
        self.UNSPSC = UNSPSC
        self.Price = Price

    def __repr__(self):
        return self.ID + "\t\t\t" + self.UNSPSC + "\t\t\t" + self.Price


def main():
    '''
    This code is to read the file (amazonReport.txt)
    '''
    amazon_report = open("amazonReport.txt", "r")


    '''
    This code is to split the contents in amazonReport.txt file line by line.
    Then, find the index for ID, UNSPSC, and Price.
    '''

    amazon_clean_report = open("AmazonCleanReport.txt","w")
    amazon_clean_report.write("OrderID\t\t\t\tUNSPSC Code\t\t\tPurchase Price\n")

    for row in amazon_report:
        splitted_report = row.split(" ")
        if 'Price' in splitted_report:
            splitted_report[splitted_report.index('Price')] = 'Price:'

        if len(splitted_report) != 1:
            ID = splitted_report[splitted_report.index('ID:') + 1]
            UNSPSC = splitted_report[splitted_report.index('Code:') + 1]
            Price = splitted_report[splitted_report.index('Price:') + 1]

        '''
        This code is to write/add to the new file (AmazonCleanReport.txt)
        '''
    
        a_list = Report(ID, UNSPSC, Price)

        amazon_clean_report = open("AmazonCleanReport.txt","a")
        amazon_clean_report.write(str(a_list))

    '''
    This code is to close both of the files (amazon_report and amazon_clean_report)
    '''
    amazon_report.close()
    amazon_clean_report.close()

main()

