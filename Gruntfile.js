module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    sass: { // config is set within the sassify-method
      options: {
        includePaths: ["static/scss/"]
      }
    },

    watch: {
      css: {
        files: ['static/scss/**/*.scss', 'apps/**/*.scss'],
        tasks: ['sassify:dev']
      }
    }
  });


  grunt.registerTask("sassify", "Finds and converts stylesheets within all apps and the main.scss.", function(n) {
    var outputStyles = {
      dev: 'expanded',
      prod: 'compressed',
    };
    // choose output-style by running grunt sassify:dev/dist. Default is nested
    var output = outputStyles[n] || '';
    // get all app directories
    grunt.file.expand({filter: 'isDirectory'}, 'apps/*').forEach(function (appDir) {
      // get the app name from the directory name
      var appName = appDir.substr(appDir.lastIndexOf('/')+1);
      // get all files within the 'SCSS'-directory
      grunt.file.expand({filter: 'isFile'}, appDir + '/static/' + appName + '/scss/*').forEach(function (scssPath) {
        // get scss-filename
        var fileName = scssPath.substr(scssPath.lastIndexOf('/')+1).slice(0,-5); // -5 removes '.scss'
        // create a path to the 'CSS'-directory
        var destDir = appDir + '/static/' + appName + '/css/';
        // get the current sass object from initConfig
        var sass = grunt.config.get('sass') || {};
        // compile-options
        sass[fileName] = {
          src: scssPath,
          dest: destDir + fileName + '.css',
          options: {
            outputStyle: output,
          },
        };
        // add this subtasks to the sass task in initConfig
        grunt.config.set('sass', sass);
      });
    });
    // sass main.scss
    var sass = grunt.config.get('sass') || {};
    sass['main'] = {
      src: 'static/scss/main.scss',
      dest: 'static/css/main.css',
      options: {
        outputStyle: output,
      },
    }
    grunt.config.set('sass', sass);
    // run SASS-task with given config
    grunt.task.run('sass');
  });


  // Load plugins here.
  grunt.loadNpmTasks('grunt-contrib-concat');
  // grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-sass');
  grunt.loadNpmTasks('grunt-contrib-watch');

  // Register tasks here.
  // the default task
  grunt.registerTask("default", ['watch:css']);
};