// RequireJS optimization configuration
// Full example: https://github.com/jrburke/r.js/blob/master/build/example.build.js

({
    // Optimize relative to this url (i.e. the current directory)
    baseUrl: '.',
<<<<<<< HEAD

=======
    
>>>>>>> 0e24556... Adding Containerization (Docker) and Subfolder for Continuous Integration and Deployment (CID)
    // The source directory of the modules
    appDir: 'src',

    // The target directory of the optimized modules
    dir: 'min',

    optimize: 'uglify',

    optimizeCss: 'none',

<<<<<<< HEAD
    loglevel: 1,

    throwWhen: {
        combined: true
    },

    paths: {
        'project': '.',
        'cilantro': 'empty:',
        'jquery': 'empty:',
        'underscore': 'empty:',
        'backbone': 'empty:',
        'mariontette': 'empty:',
        'highcharts': 'empty:',
        'bootstrap': 'empty:'
    },

    name: 'main'
=======
    paths: {
        'cilantro': 'empty:',
        'project': '.'
    },

    name: 'main'

>>>>>>> 0e24556... Adding Containerization (Docker) and Subfolder for Continuous Integration and Deployment (CID)
})
