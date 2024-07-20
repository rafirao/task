from flask import Flask, request

app = Flask(__name__)

def convert_value(value, input_format, output_format):
    if input_format == "dec":
        dec_value = int(value)
    elif input_format == "bin":
        dec_value = int(value, 2)
    elif input_format == "hex":
        dec_value = int(value, 16)
    else:
        return "Invalid input format"

    if output_format == "dec":
        return str(dec_value)
    elif output_format == "bin":
        return bin(dec_value)[2:]
    elif output_format == "hex":
        return hex(dec_value)[2:]
    else:
        return "Invalid output format"

@app.route('/convert/<value>/<input_format>/<output_format>', methods=['GET'])
def convert(value, input_format, output_format):
    try:
        result = convert_value(value, input_format, output_format)
        return result
    except ValueError:
        return "Invalid value for the specified input format", 400

@app.route('/health', methods=['GET'])
def health_check():
    return "OK"

@app.route('/', methods=['GET'])
def usage():
    return """
    Usage: /convert/<value>/<input_format>/<output_format>
    <value>: Any alphanumeric value in the specified input format.
    <input_format>: dec, bin, or hex.
    <output_format>: dec, bin, or hex.
    """

@app.errorhandler(404)
def page_not_found(e):
    return """
    Usage: /convert/<value>/<input_format>/<output_format>
    <value>: Any alphanumeric value in the specified input format.
    <input_format>: dec, bin, or hex.
    <output_format>: dec, bin, or hex.
    """, 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
