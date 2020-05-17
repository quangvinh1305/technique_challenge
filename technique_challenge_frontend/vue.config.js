const path = require('path');
module.exports = {
  "transpileDependencies": [
    "vuetify"
  ],
  configureWebpack: {
		resolve: {
	    alias: {
	      Constants: path.resolve(__dirname, 'src/constants/'),
	    },
	    extensions: ['*', '.js', '.vue', '.json']
    },

  }

}