from crewai_instapost.crew import CrewaiInstapost

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic':"AI Agents in Real-World Applications"
    }

    try:
        CrewaiInstapost().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
