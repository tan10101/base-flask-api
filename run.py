from app import create_app

if __name__ == '__main__':
  config_name = 'testing'
  app = create_app(config_name)
  app.run(debug=True, host='0.0.0.0')
