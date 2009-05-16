import matcher_lib
import optimization_lib

def run():
    """ The main entry point """
#    parameters = {"lenders" : {"1": {"minimum_rate" : 0.05, "minimum_amount" : 100, "maximum_amount" : 1000},
#                               "2": {"minimum_rate" : 0.06, "minimum_amount" : 200, "maximum_amount" : 200},
#                               "3": {"minimum_rate" : 0.07, "minimum_amount" : 300, "maximum_amount" : 450}},
#                  "borrowers" : {"4": {"maximum_rate" : 0.08, "minimum_amount" : 100, "maximum_amount" : 100},
#                                 "5": {"maximum_rate" : 0.09, "minimum_amount" : 200, "maximum_amount" : 250},
#                                 "6": {"maximum_rate" : 0.10, "minimum_amount" : 300, "maximum_amount" : 300}}}
#    parameters = {"lenders" : {"1": {"minimum_rate" : 0.05, "minimum_amount" : 10, "maximum_amount" : 100},
#                               "2": {"minimum_rate" : 0.04, "minimum_amount" : 20, "maximum_amount" : 200},
#                               "3": {"minimum_rate" : 0.03, "minimum_amount" : 30, "maximum_amount" : 300}},
#                  "borrowers" : {"4": {"maximum_rate" : 0.15, "minimum_amount" : 10, "maximum_amount" : 100},
#                                 "5": {"maximum_rate" : 0.10, "minimum_amount" : 20, "maximum_amount" : 200},
#                                 "6": {"maximum_rate" : 0.01, "minimum_amount" : 30, "maximum_amount" : 300}}}
    parameters = {"lenders" : {"1": {"minimum_rate" : 0.05, "minimum_amount" : 10, "maximum_amount" : 100},
                               "2": {"minimum_rate" : 0.04, "minimum_amount" : 20, "maximum_amount" : 200},
                               "3": {"minimum_rate" : 0.03, "minimum_amount" : 30, "maximum_amount" : 300}},
                  "borrowers" : {"4": {"maximum_rate" : 0.15, "minimum_amount" : 10, "maximum_amount" : 100},
                                 "5": {"maximum_rate" : 0.10, "minimum_amount" : 20, "maximum_amount" : 200},
                                 "6": {"maximum_rate" : 0.01, "minimum_amount" : 30, "maximum_amount" : 300}}}

    # create the generator
    solution_generator = matcher_lib.MatcherSolutionGenerator(parameters)

    # create the evaluator, using the tight margin utility function
    solution_evaluator = matcher_lib.MatcherSolutionEvaluator(matcher_lib.MatcherSolutionEvaluator.tight_margin_utility)

    # create the visualizer
    solution_visualizer = matcher_lib.MatcherSolutionVisualizer()

    # create the coordinator, injecting the created objects
    #optimizer = optimization_lib.Optimizer(solution_generator, solution_evaluator, solution_visualizer)
    optimizer = optimization_lib.HillClimbingOptimizer(solution_generator, solution_evaluator, solution_visualizer)

    optimizer.set_budget(100)

    # run the coordinator
    solution = optimizer.optimize()

    print "--"
    print "FINAL SOLUTION"

    # evaluate the final solution
    utility = solution_evaluator.evaluate(parameters, solution)

    # display the results
    solution_visualizer.display(parameters, solution, utility)


# run the solver
run()
