X = list(map(int, input("Enter Space Separated X values:\n").split()))
Y = list(map(int, input("Enter Space Separated Y values:\n").split()))

meanx = sum(X)/len(X)
meany = sum(Y)/len(X)

xiyi = sum((X[i]*Y[i] for i in range(len(X))))
xsqr = sum((X[i]**2 for i in range(len(X))))

B1 = (xiyi - len(X)*meanx*meany) / (xsqr - len(X)*meanx*meanx)
B0 = meany - B1*meanx

SSTsum = sum((Y[i] - meany)**2 for i in range(len(X)))
SSEsum = sum((Y[i] - (B0 + B1*X[i]))**2 for i in range(len(X)))
SSRsum = sum(((B0 + B1*X[i]) - meany)**2 for i in range(len(X)))

print("x\ty\tx2\txy\tYp\tSST\tSSE\tSSR")
print("------------------------------------------------------------")
for i in range(len(X)):
    print("{}\t{}\t{}\t{}\t{:.2f}\t{:.2f}\t{:.2f}\t{:.2f}".format(X[i], Y[i], X[i]**2, X[i]*Y[i], B0 + B1*X[i],(Y[i] - meany)**2, (Y[i] - (B0 + B1*X[i]))**2, ((B0 + B1*X[i]) - meany)**2))
print("------------------------------------------------------------")
print("{}\t{}\t{}\t{}\t{}\t{:.2f}\t{:.2f}\t{:.2f}".format(sum(X), sum(Y), xsqr, xiyi, " ", SSTsum, SSEsum, SSRsum))
print()

print("Mean X: {}".format(meanx))
print("Mean Y: {}\n".format(meany))
print("B0: {}".format(B0))
print("B1: {}\n".format(B1))
print("Regression Equation: y = {:.3f} + {:.3f}x\n\n".format(B0, B1))
print("R2 = SSR/SST = {:.4f}".format(SSRsum/SSTsum))
