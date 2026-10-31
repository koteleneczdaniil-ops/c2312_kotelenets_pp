import warnings

warnings.simplefilter('ignore', SyntaxWarning)
warnings.simplefilter('always', ImportWarning)

warnings.warn('warnings,no code here', SyntaxWarning)
warnings.warn('warnings,module not imported', ImportWarning)


