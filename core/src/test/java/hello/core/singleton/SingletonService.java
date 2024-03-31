package hello.core.singleton;

public class SingletonService {
	
	private static final SingletonService instance = new SingletonService();
	
	public static SingletonService getInstance() {
		return instance;
	}
	
	//private 생성자 -> 외부에서 객체 생성 못 하도록 막음
	private SingletonService() {
	}
	
	public void logic() {
		System.out.println("Singleton 객체 로직 호출");
	}
}
