
import router
import databasecontroller as dbc


if __name__ == "__main__":
        app = router.init()
        dbc.init(dbupdate=True)
        app.run(debug=True)
